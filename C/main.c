#include <stdlib.h>
#include <stdio.h>
#include "SDL.h"
#include "drawline.h"
#include "triangle.h"
#include "teapot_data.h"

triangle_t exampletriangle1 = {
    .x1 = 100,
    .y1 = 200,
    .x2 = 200,
    .y2 = 100,
    .x3 = 300,
    .y3 = 300,
    .fillcolor = 0xffff0000,
    .scale = 1.0
};

triangle_t exampletriangle2 = {
    .x1 = 50,
    .y1 = 150,
    .x2 = 150,
    .y2 = 50,
    .x3 = 250,
    .y3 = 250,
    .fillcolor = 0xffffff00,
    .scale = 1.0
};

triangle_t exampletriangle3 = {
    .x1 = 350,
    .y1 = 350,
    .x2 = 460,
    .y2 = 300,
    .x3 = 500,
    .y3 = 400,
    .fillcolor = 0xff00ff00,
    .scale = 1.0
};

triangle_t exampletriangle4 = {
    .x1 = 350,
    .y1 = 100,
    .x2 = 450,
    .y2 = 50,
    .x3 = 500,
    .y3 = 200,
    .fillcolor = 0xff0000ff,
    .scale = 1.0
};

// First function run in your program
int main(int argc, char **argv)
{
    int retval, done;
    SDL_Surface *screen;
    SDL_Event event;
    
    // Initialize SDL   
    retval = SDL_Init(SDL_INIT_VIDEO);
    if (retval == -1) {
        printf("Unable to initialize SDL\n");
        exit(1);    
    }
    
    //Create a 1024x768x32 window
    screen = SDL_SetVideoMode(1024, 768, 32, 0);     
    if (screen == NULL) {
        printf("Unable to get video surface: %s\n", SDL_GetError());    
        exit(1);
    }


    // The teapot is represented as an array of triangle data structures.
    // To draw it on the screen you need to traverse the 'teapot_model' array
    // and call DrawTriangle for each triangle (teapot_data.h contains the array).  
    // The definition TEAPOT_NUMTRIANGLES specifies the number of triangles in the array.
    // The teapot model is contained within a 1000x1000 box (coordinates
    // from -500 to 500 on the x and y axis).  Remember to translate the
    // model to the middle of the screen before drawing it (initialize 
    // triangle->tx and triangle->ty with the appropriate coordinates).
    
    
    // Draw some example triangles on the screen. 
    // Use these examples in the beginning.
    
    // Flush events
    while(SDL_PollEvent(&event));

    DrawTriangle(screen, &exampletriangle1);
    DrawTriangle(screen, &exampletriangle2);
    DrawTriangle(screen, &exampletriangle3);
    DrawTriangle(screen, &exampletriangle4);

    done = 0;
    while (done == 0) {
        while (SDL_PollEvent(&event)) {
            switch (event.type) {
            case SDL_QUIT:
                done = 1;
                break;  
            }           
        }
    }   
    
    SDL_Quit();

    return 0;
}

