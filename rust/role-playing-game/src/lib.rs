// This stub file contains items which aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

pub struct Player {
    pub health: u32,
    pub mana: Option<u32>,
    pub level: u32,
}

impl Player {
    pub fn revive(&self) -> Option<Player> {
        if self.health == 0 {
            if self.level >= 10 {
                return Some(Player {
                    health: 100,
                    mana: Some(100),
                    level: self.level,
                });
            } else {
                return Some(Player {
                    health: 100,
                    mana: None,
                    level: self.level,
                });
            }
        }
        None
    }

    pub fn cast_spell(&mut self, mana_cost: u32) -> u32 {
        match self.mana {
            Some(mana) => {
                if mana >= mana_cost {
                    self.mana = Some(mana - mana_cost);
                    mana_cost * 2
                } else {
                    0
                }
            }
            None => {
                let new_health = if (self.health >= mana_cost) {
                    self.health - mana_cost
                } else {
                    0
                };
                self.health = new_health;
                0
            }
        }
    }
}
