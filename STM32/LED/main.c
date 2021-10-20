/*
新建一个寄存器版本工程
PB地址 0x40020400~0x400207ff
*/

//简易LED点亮程序 点亮连接PB1端口的LED,其已接入外部电源高电平，故设置
//pb1为低电平即可



#include "stm32f4xx.h"

/*
#define GPIOB (unsigned int *)0x40020400
#define GPIOB_MODER (unsigned int *)(GPIOB +0x00)
#define GPIOB_ODR (unsigned int *)(GPIOB+0x14)
typedef unsigned int* un_s32;

int main()
{
	
	//打开pb端口时钟
	*RCC_AHB1ENR |=1<<1;

	//将pb端口的模式改为普通输出
	*GPIOB_MODER |= 0B101;
	//将pb1的输出改为0，输出数据寄存器将输出设置为低电平
	*GPIOB_ODR &=~0B01;
	return 0;
	
}
*/



//寄存器点亮LED灯2
#define GPIOB (unsigned int*)0x40020400
#define GPIOB_MODER (unsigned int*)(GPIOB+0x00)
#define GPIOB_ODR (unsigned int*)(GPIOB+0x14)
#define GPIOB_PUPDR (unsigned int*)(GPIOB+0x0c)
#define GPIOB_OSPEEDR (unsigned int*)(GPIOB+0X08)
#define GPIOB_OTYPER (unsigned int*)(GPIOB+0X04)
#define GPIOB_BSRR (unsigned int*)(GPIOB +0X18)
#define GPIOB_LOCK (unsigned int*)(GPIOB +0x1c)

int main(void)
{
	//*GPIOB_ODR |=0X03;
	//第一步打开PB的时钟，打开时钟必须是第一步，不然前面面编码无效
	*RCC_AHB1ENR |=1<<1;
	//第二步设置GPIO_B1的模式，设置为输出模式(01)
	//清空先
	//*GPIOB_MODER &=~0X0F;
	//*GPIOB_MODER |=0X01;

	
	//第三步设置上拉 电阻(01上拉)
	//*GPIOB_PUPDR &=~0x0f;
	//*GPIOB_PUPDR |=0x05;
	//设置速度 低速（00）
	//*GPIOB_OSPEEDR &=~0X0F;
	//设置推挽输出类型0为推挽
	//*GPIOB_OTYPER =0x00;
	//*GPIOB_ODR |=15;
	//*GPIOB_ODR |=1;
	//*GPIOB_BSRR =0X00;
	
	*GPIOB_MODER =0x00000005;
	*GPIOB_OTYPER =0X00000000;
	*GPIOB_OSPEEDR =0X0000000F;
	*GPIOB_LOCK = 0x00000000;
	*GPIOB_PUPDR = 0X00000005;
	//*GPIOB_BSRR = 0X00000000;
	*GPIOB_ODR |=1;

}

void SystemInit(void)
{
	
}
