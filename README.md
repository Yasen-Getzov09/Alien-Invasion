# 👾 Alien Invasion

![Alien Invasion](https://images.unsplash.com/photo-1549921296-3a73e218a6b0?auto=format&fit=crop&w=1200&q=80)

A classic arcade-style **space shooter** game built using **Python** and **Pygame**, inspired by the *Alien Invasion* project from *Python Crash Course* by Eric Matthes.

---

## 🎮 Game Overview

In **Alien Invasion**, you control a spaceship that must shoot down waves of incoming aliens. The game features smooth motion, collision detection, score tracking, and increasing difficulty with each wave.

---

## 🚀 Features

- 🛸 Smooth player movement with keyboard controls  
- 💥 Bullet and alien collision detection  
- 🧠 Scoreboard with current score and high score tracking  
- 📈 Increasing difficulty over time  
- ❤️ Ship icons representing player lives  
- 🔊 Sound effects (optional)

---

## 🕹️ Controls

| Action        | Key       |
|---------------|-----------|
| Move Left     | ← Arrow   |
| Move Right    | → Arrow   |
| Fire Bullet   | Spacebar  |
| Quit Game     | Q         |

---

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/alien-invasion.git
   cd alien-invasion
   ```

2. Install the required libraries:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python alien_invasion.py
   ```

---

## 🗂️ Project Structure

```
alien_invasion/
│
├── alien.py
├── bullet.py
├── button.py
├── game_stats.py
├── scoreboard.py
├── settings.py
├── ship.py
├── alien_invasion.py
└── images/
    └── ship.bmp
    └── alien.png
    └── background.jpg

```

---

## 🧠 Based On

This game is based on the **Alien Invasion** project in the book:  
📘 *Python Crash Course* by Eric Matthes – 2nd Edition

---

## 📜 License

This project is open source under the [MIT License](LICENSE).

---

## ✨ Customize the Game

Want to change the background image?

1. Replace your background image file (e.g., `background.jpg`) in the `images/` folder.
2. In your main game file (e.g., `alien_invasion.py`), load your new image:

```python
self.bg_image = pygame.image.load('images/your_background.jpg')
```

---

Happy coding! 🚀