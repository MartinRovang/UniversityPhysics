import numpy as np



def colormapping(Image, values, colors):
    """
    Image -> numpy array
    values = [0,1,2,3,4,5,6,...]\n
    colors = {'red': [2,5,1,81,12,43,8,..], 'green': [2,5,1,81,12,43,8,..], 'blue': [2,5,1,81,12,43,8,..]}

    maps values 0,1,.... to color red2,5,...+ green2,5,... + blue,2,5,....
    Example: 0 intensity will map to color (2, 2, 2) (RGB) etc.
    If not specified it turns black -> (0, 0, 0).
    # """

    try:
        a,b = Image.shape
        NewfigRed = np.zeros((a,b))
        NewfigGreen = np.zeros((a,b))
        NewfigBlue = np.zeros((a,b))
        Newfig = np.zeros((a,b,3))
        for counter, value in enumerate(values):
            dx = np.where(Image == value)
            for color in colors:
                if color == 'red':
                    NewfigRed[dx] = colors[color][counter]
                if color == 'green':
                    NewfigGreen[dx] = colors[color][counter]
                if color == 'blue':
                    NewfigBlue[dx] = colors[color][counter]

        Newfig[:,:,0] = NewfigRed
        Newfig[:,:,1] = NewfigGreen
        Newfig[:,:,2] = NewfigBlue

        return Newfig.astype('uint8')
    except Exception as e:
        print(e)
        print('Dictionary lists(colors) and values list must have same length!')