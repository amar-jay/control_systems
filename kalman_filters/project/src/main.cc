#include "display.h"
#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>
#include <eigen3/Eigen/Dense>
#include <iostream>

int main(int argc, char *args[]) {
  // Initialize SDL
  if (SDL_Init(SDL_INIT_VIDEO) < 0) {
    std::cerr << "SDL could not initialize! SDL_Error: " << SDL_GetError()
              << std::endl;
    return -1;
  }

  // Initialize SDL_ttf
  if (TTF_Init() == -1) {
    std::cerr << "TTF could not initialize! TTF_Error: " << TTF_GetError()
              << std::endl;
    SDL_Quit();
    return -1;
  }

  Display mDisplay;
  if (!mDisplay.createRenderer("AKFSF Simulations", SCREEN_WIDTH,
                               SCREEN_HEIGHT)) {
    return -1;
  }

  bool running = true;
  while (running) {

    mDisplay.clearScreen();

    mDisplay.showScreen();

    SDL_Event event;
    while (SDL_PollEvent(&event) != 0) {
      if (event.type == SDL_QUIT) {
        running = false;
      }
    }
  }

  // Eigen3 example
  Eigen::Matrix3f A;
  A << 1, 2, 3, 4, 5, 6, 7, 8, 9;
  std::cout << "Matrix A:\n" << A << std::endl;

  std::cout << "Successfilly initialized all" << std::endl;

  // Clean up
  mDisplay.destroyRenderer();
  TTF_Quit();
  SDL_Quit();
  return 0;
}
