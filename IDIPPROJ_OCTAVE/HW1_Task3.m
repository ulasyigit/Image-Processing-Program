pkg load image

clear all;
close all;
clc;
a = imread('leo.jpg');
subplot(2,2,1), imshow(a),title('Original Image');
b = imrotate(a, 90);
subplot(2,2,2), imshow(b),title('Rotated Image');
subplot(2,2,3), c=rgb2gray(a), imshow(c),title('Grayscale');
subplot(2,2,4), imhist(c),title('histogram');
