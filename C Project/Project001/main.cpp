#include <stdio.h>

struct tj
{
	int a;
	char b;
	float c;
};

int main()
{
	struct tj b1;
	b1.a = 2;
	b1.b = 'g';
	b1.c = 2.36;
	struct tj* p1 = &b1;
	int a1 = b1.a;
	int* p2 = &b1.a;
	int* p3 = &a1;
	p1->c = b1.c + 0.7;
	printf("%d-%c-%f-%p-%p-%p",b1.a,b1.b,b1.c,p1,p2,p3);



	return 0;
}