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


#include <graphics.h>              // ����ͼ�ο�ͷ�ļ�
#include <conio.h>
int main()
{
	initgraph(640, 480);            // ������ͼ���ڣ���СΪ 640x480 ����
	setlinecolor(RGB(255, 0, 0));   // ���õ�ǰ������ɫ
	setfillcolor(RGB(0, 255, 0));   // ���õ�ǰ�����ɫ
	fillcircle(200, 200, 100);      // ��Բ��Բ��(200, 200)���뾶 100
	_getch();                       // �����������
	closegraph();                   // �ر�ͼ�λ���
}