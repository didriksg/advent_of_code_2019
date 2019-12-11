import matplotlib.pyplot as plt
import numpy as np


def split_into_layers(data, layer_size):
    index = 0
    layers = []
    for i in range(0, len(data), layer_size):
        layer = data[i:i + layer_size]
        layers.append(layer)

    return layers


def find_most_zeros(layers):
    smallest_layer = None
    zero_count = np.math.inf
    for layer in layers:
        zeros = layer.count('0')
        if zeros < zero_count:
            zero_count = zeros
            smallest_layer = layer

    return smallest_layer, zero_count


def decode_image(layers, layer_size):
    final_image = np.full(shape=(6, 25), fill_value=2)
    for layer in layers:
        j = -1
        for i, pixel in enumerate(list(layer)):
            pos = i % 25
            if pos == 0:
                j += 1
            pixel = int(layer[i])
            if pixel != 2 and final_image[j, pos] != 1 and final_image[j, pos] != 0:
                final_image[j, pos] = pixel
    return np.uint8(final_image)


test_input = open('input.txt').read()
layers = split_into_layers(test_input, 25 * 6)
layer, zeros = find_most_zeros(layers)
unique, count = np.unique(list(layer), return_counts=True)
print(layer, zeros)
print(unique, count)
print(count[1] * count[2])

final_image = decode_image(layers, 25 * 6)
plt.imshow(final_image, cmap='gray')
plt.show()
