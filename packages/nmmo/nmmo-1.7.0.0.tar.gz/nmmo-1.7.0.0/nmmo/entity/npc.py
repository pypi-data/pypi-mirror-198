
import random

from nmmo.entity import entity
from nmmo.io import action as Action
from nmmo.lib.colors import Neon
from nmmo.systems import combat, droptable
from nmmo.systems.ai import policy
from nmmo.systems import item as Item
from nmmo.systems import skill
from nmmo.systems.inventory import EquipmentSlot


class Equipment:
  def __init__(self, total,
    melee_attack, range_attack, mage_attack,
    melee_defense, range_defense, mage_defense):

    self.level         = total
    self.ammunition    = EquipmentSlot()

    self.melee_attack  = melee_attack
    self.range_attack  = range_attack
    self.mage_attack   = mage_attack
    self.melee_defense = melee_defense
    self.range_defense = range_defense
    self.mage_defense  = mage_defense

  def total(self, getter):
    return getter(self)

  # pylint: disable=R0801
  # Similar lines here and in inventory.py
  @property
  def packet(self):
    packet = {}

    packet['item_level']    = self.total
    packet['melee_attack']  = self.melee_attack
    packet['range_attack']  = self.range_attack
    packet['mage_attack']   = self.mage_attack
    packet['melee_defense'] = self.melee_defense
    packet['range_defense'] = self.range_defense
    packet['mage_defense']  = self.mage_defense

    return packet


class NPC(entity.Entity):
  def __init__(self, realm, pos, iden, name, color, pop):
    super().__init__(realm, pos, iden, name, color, pop)
    self.skills = skill.Combat(realm, self)
    self.realm = realm
    self.last_action = None
    self.droptable = None
    self.spawn_danger = None
    self.equipment = None

  def update(self, realm, actions):
    super().update(realm, actions)

    if not self.alive:
      return

    self.resources.health.increment(1)
    self.last_action = actions

  # Returns True if the entity is alive
  def receive_damage(self, source, dmg):
    if super().receive_damage(source, dmg):
      return True

    # run the next lines if the npc is killed
    # source receive gold & items in the droptable
    # pylint: disable=no-member
    source.gold.increment(self.gold.val)
    self.gold.update(0)

    # TODO(kywch): make source receive the highest-level items first
    #   because source cannot take it if the inventory is full
    #   Also, destroy the remaining items if the source cannot take those
    for item in self.droptable.roll(self.realm, self.attack_level):
      if source.inventory.space:
        source.inventory.receive(item)

    return False

  @staticmethod
  def spawn(realm, pos, iden):
    config = realm.config

    # Select AI Policy
    danger = combat.danger(config, pos)
    if danger >= config.NPC_SPAWN_AGGRESSIVE:
      ent = Aggressive(realm, pos, iden)
    elif danger >= config.NPC_SPAWN_NEUTRAL:
      ent = PassiveAggressive(realm, pos, iden)
    elif danger >= config.NPC_SPAWN_PASSIVE:
      ent = Passive(realm, pos, iden)
    else:
      return None

    ent.spawn_danger = danger

    # Select combat focus
    style = random.choice((Action.Melee, Action.Range, Action.Mage))
    ent.skills.style = style

    # Compute level
    level = 0
    if config.PROGRESSION_SYSTEM_ENABLED:
      level_min = config.NPC_LEVEL_MIN
      level_max = config.NPC_LEVEL_MAX
      level     = int(danger * (level_max - level_min) + level_min)

      # Set skill levels
      if style == Action.Melee:
        ent.skills.melee.set_experience_by_level(level)
      elif style == Action.Range:
        ent.skills.range.set_experience_by_level(level)
      elif style == Action.Mage:
        ent.skills.mage.set_experience_by_level(level)

    # Gold
    if config.EXCHANGE_SYSTEM_ENABLED:
      # pylint: disable=no-member
      ent.gold.update(level)

    ent.droptable = droptable.Standard()

    # Equipment to instantiate
    if config.EQUIPMENT_SYSTEM_ENABLED:
      lvl     = level - random.random()
      ilvl    = int(5 * lvl)

      offense = int(config.NPC_BASE_DAMAGE + lvl*config.NPC_LEVEL_DAMAGE)
      defense = int(config.NPC_BASE_DEFENSE + lvl*config.NPC_LEVEL_DEFENSE)

      ent.equipment = Equipment(ilvl, offense, offense, offense, defense, defense, defense)

      armor =  [Item.Hat, Item.Top, Item.Bottom]
      ent.droptable.add(random.choice(armor))

    if config.PROFESSION_SYSTEM_ENABLED:
      tools =  [Item.Rod, Item.Gloves, Item.Pickaxe, Item.Chisel, Item.Arcane]
      ent.droptable.add(random.choice(tools))

    return ent

  def packet(self):
    data = super().packet()

    data['skills']   = self.skills.packet()
    data['resource'] = {'health': self.resources.health.val}

    return data

  @property
  def is_npc(self) -> bool:
    return True

class Passive(NPC):
  def __init__(self, realm, pos, iden):
    super().__init__(realm, pos, iden, 'Passive', Neon.GREEN, -1)

  def decide(self, realm):
    return policy.passive(realm, self)

class PassiveAggressive(NPC):
  def __init__(self, realm, pos, iden):
    super().__init__(realm, pos, iden, 'Neutral', Neon.ORANGE, -2)

  def decide(self, realm):
    return policy.neutral(realm, self)

class Aggressive(NPC):
  def __init__(self, realm, pos, iden):
    super().__init__(realm, pos, iden, 'Hostile', Neon.RED, -3)

  def decide(self, realm):
    return policy.hostile(realm, self)
