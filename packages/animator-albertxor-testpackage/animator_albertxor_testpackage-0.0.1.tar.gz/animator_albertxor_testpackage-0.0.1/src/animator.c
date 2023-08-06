#include <SDL2/SDL.h>


const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;


int main() {

    if(SDL_Init(SDL_INIT_EVERYTHING) != 0) return 1;

    SDL_Surface* screen_surface = NULL;
    SDL_Window* window = NULL;

    window = SDL_CreateWindow("The Animator");

    return 0;
}
