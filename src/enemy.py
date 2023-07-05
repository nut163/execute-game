```python
class Enemy:
    def __init__(self, sprite, health, damage, speed):
        self.sprite = sprite
        self.health = health
        self.damage = damage
        self.speed = speed

    def move(self, direction):
        if direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed
        elif direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed

    def attack(self, player_character):
        player_character.health -= self.damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        enemies.remove(self)

def load_enemies():
    with open('assets/enemies/enemy_sprites.png', 'r') as file:
        enemy_sprites = file.read().splitlines()
    for sprite in enemy_sprites:
        enemies.append(Enemy(sprite, 100, 10, 2))
```
