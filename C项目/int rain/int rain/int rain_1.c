#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <graphics.h>
#define WIDTH 1280
#define HEIGTH 1080
#define STR_SIZE 32
struct bety
{
	int x;
	int y;
	char bety_num[STR_SIZE]

 };

int main()
{
	initgraph(WIDTH, HEIGTH);
	return 0;
}