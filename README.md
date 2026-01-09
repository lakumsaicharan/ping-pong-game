# 🏓 Ping Pong Game

A classic two-player Ping Pong (Pong) game implemented in Python using the Turtle graphics library. Experience the nostalgia of one of the first arcade video games ever created!

## 📋 Description

This is a recreation of the iconic Pong arcade game where two players control paddles on opposite sides of the screen, competing to keep the ball in play. The game features smooth paddle movement, realistic ball physics with bouncing mechanics, and an automatic scoring system that tracks each player's points.

## ✨ Features

- 🎮 **Two-Player Gameplay**: Classic head-to-head competition
- 🎯 **Smooth Controls**: Responsive keyboard controls for both players
- ⚽ **Realistic Physics**: Ball bounces off paddles and walls with proper angles
- 🏆 **Score Tracking**: Real-time scoreboard displays both players' scores
- 🔄 **Auto-Serve**: Ball automatically resets after each point
- 🎨 **Clean Graphics**: Simple, elegant retro-style visuals
- 🚀 **Fast-Paced Action**: Increasing ball speed for exciting gameplay

## 🎮 Game Controls

### Player 1 (Right Paddle)
- **W**: Move paddle up
- **S**: Move paddle down

### Player 2 (Left Paddle)
- **Up Arrow**: Move paddle up
- **Down Arrow**: Move paddle down

## 🎯 Game Rules

1. Each player controls a paddle on their side of the screen
2. The ball bounces between the paddles and walls
3. If a player misses the ball, their opponent scores a point
4. The ball automatically resets to the center after each point
5. First player to reach the target score wins!

## 🛠️ Technologies Used

- **Python 3.x**
- **Turtle Graphics Module**: Built-in Python library for graphics and animation
- **Object-Oriented Programming**: Modular class-based architecture

## 📁 Project Structure

```
ping-pong-game/
│
├── main.py              # Main game loop and screen setup
├── paddle.py            # Paddle class with movement logic
├── ball.py              # Ball class with physics and collision detection
├── score.py             # Scoreboard class for score tracking and display
├── LICENSE              # MIT License
└── README.md            # Project documentation
```

## 🚀 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lakumsaicharan/ping-pong-game.git
   cd ping-pong-game
   ```

2. **Ensure Python is installed**:
   ```bash
   python --version
   ```
   *Note: Python 3.x is required*

3. **Run the game**:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. **Start the Game**: Run `main.py` to launch the game window
2. **Player 1 (Right)**: Use W/S keys to move your paddle
3. **Player 2 (Left)**: Use Up/Down arrow keys to move your paddle
4. **Keep the Ball in Play**: Hit the ball with your paddle to send it back
5. **Score Points**: Make your opponent miss the ball
6. **Watch the Score**: Top of the screen shows current scores
7. **Play Until Victory**: First to the winning score takes the match!

## 💡 Game Mechanics

- **Paddle Movement**: Vertical movement within screen boundaries
- **Ball Physics**: 
  - Bounces off top and bottom walls
  - Bounces off paddles when contact is made
  - Resets to center when it passes a paddle
- **Collision Detection**: Detects when ball hits paddles or walls
- **Scoring System**: Points awarded when opponent misses
- **Ball Speed**: Gradually increases after each paddle hit

## 🎓 Learning Objectives

This project demonstrates:
- ✅ Object-Oriented Programming (OOP) with multiple classes
- ✅ Game loop implementation
- ✅ Event handling for keyboard input
- ✅ Collision detection algorithms
- ✅ 2D physics simulation
- ✅ Score tracking and UI updates
- ✅ Modular code design

## 🔧 Customization Ideas

- Adjust ball speed by modifying the ball movement values
- Change paddle size for different difficulty levels
- Add sound effects for ball hits and scoring
- Implement AI for single-player mode
- Add power-ups or special effects
- Create different visual themes

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests
- 🎨 Improve graphics or gameplay

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Lakum Sai Charan**
- GitHub: [@lakumsaicharan](https://github.com/lakumsaicharan)
- Part of the 100 Days of Code Challenge

## 🙏 Acknowledgments

- Inspired by the original Pong arcade game (1972)
- Built as part of Python learning journey
- Thanks to the Python Turtle graphics community
- Classic game mechanics adapted for modern Python

## 🎮 Fun Fact

Pong was one of the earliest arcade video games and helped establish the video game industry. This Python recreation captures the simple yet addictive gameplay that made the original a classic!

---

⭐ **Enjoyed the game? Give it a star!** ⭐

*Challenge a friend and see who becomes the Pong champion!* 🏆
