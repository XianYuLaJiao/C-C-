//#define _CRT_SECURE_NO_WARNINGS 1
//#include <stdio.h>
//#include <graphics.h>
//#define WIDTH 1280
//#define HEIGTH 1080
//#define STR_SIZE 32
//struct bety
//{
//	int x;
//	int y;
//	char bety_num[STR_SIZE];
//};
//
//int main()
//{
//	initgraph(WIDTH, HEIGTH);
//	return 0;
//}
//


#include <graphics.h>              // 引用图形库头文件
#include <conio.h>
int main()
{
	initgraph(640, 480);            // 创建绘图窗口，大小为 640x480 像素
	setlinecolor(RGB(255, 0, 0));   // 设置当前线条颜色
	setfillcolor(RGB(0, 255, 0));   // 设置当前填充颜色
	fillcircle(200, 200, 100);      // 画圆，圆心(200, 200)，半径 100
	_getch();                       // 按任意键继续
	closegraph();                   // 关闭图形环境
}