#ifndef INCLUDE_PROJECT_DISPLAY_H
#define INCLUDE_PROJECT_DISPLAY_H
#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>
#include <eigen3/Eigen/Core>
#include <eigen3/Eigen/src/Core/Matrix.h>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

#define SCREEN_WIDTH 1024
#define SCREEN_HEIGHT 768
#define GRID_SIZE 500
#define GRID_SPACEING 25

struct Vector2 {
  double x, y;
  Vector2() = default; // Default constructor
  Vector2(double x, double y) : x(x), y(y) {}
};

class Display {
public:
  Display();
  ~Display();

  bool createRenderer(std::string title, int screenWidth, int screenHeight);
  void destroyRenderer();

  void setDrawColour(uint8_t red, uint8_t green, uint8_t blue,
                     uint8_t alpha = 0xFF);
  void setView(double width, double height, double xOffset, double yOffset);
  void setView(double xOffset, double yOffset);
  void drawLine(const Vector2 &startPos, const Vector2 &endPos);
  void drawLines(const std::vector<Vector2> &points);
  void drawLines(const std::vector<std::vector<Vector2>> &points);

  void showScreen();
  void clearScreen();

private:
  int mScreenWidth;
  int mScreenHeight;

  double mViewWidth;
  double mViewHeight;
  double mViewXOffset;
  double mViewYOffset;

  SDL_Window *mWindow;
  SDL_Renderer *mRenderer;
  TTF_Font *mMainFont;
};

// transform single vector
std::vector<Eigen::Vector2d>
transformPoints(const std::vector<Eigen::Vector2d> &points,
                const Eigen::Vector2d &position, const double rotation);

// transform entire dataset
std::vector<std::vector<Eigen::Vector2d>>
transformPoints(const std::vector<std::vector<Eigen::Vector2d>> &dataset,
                const Eigen::Vector2d &position, const double rotation);

// offset single vector
std::vector<Eigen::Vector2d>
offsetPoints(const std::vector<Eigen::Vector2d> &points,
             const Eigen::Vector2d &offset);

// offset entire dataset
std::vector<std::vector<Eigen::Vector2d>>
offsetPoints(const std::vector<std::vector<Eigen::Vector2d>> &dataset,
             const Eigen::Vector2d &offset);

#endif
