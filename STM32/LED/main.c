/*
�½�һ���Ĵ����汾����
PB��ַ 0x40020400~0x400207ff
*/

//����LED�������� ��������PB1�˿ڵ�LED,���ѽ����ⲿ��Դ�ߵ�ƽ��������
//pb1Ϊ�͵�ƽ����



#include "stm32f4xx.h"

/*
#define GPIOB (unsigned int *)0x40020400
#define GPIOB_MODER (unsigned int *)(GPIOB +0x00)
#define GPIOB_ODR (unsigned int *)(GPIOB+0x14)
typedef unsigned int* un_s32;

int main()
{
	
	//��pb�˿�ʱ��
	*RCC_AHB1ENR |=1<<1;

	//��pb�˿ڵ�ģʽ��Ϊ��ͨ���
	*GPIOB_MODER |= 0B101;
	//��pb1�������Ϊ0��������ݼĴ������������Ϊ�͵�ƽ
	*GPIOB_ODR &=~0B01;
	return 0;
	
}
*/



//�Ĵ�������LED��2
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
	//��һ����PB��ʱ�ӣ���ʱ�ӱ����ǵ�һ������Ȼǰ���������Ч
	*RCC_AHB1ENR |=1<<1;
	//�ڶ�������GPIO_B1��ģʽ������Ϊ���ģʽ(01)
	//�����
	//*GPIOB_MODER &=~0X0F;
	//*GPIOB_MODER |=0X01;

	
	//�������������� ����(01����)
	//*GPIOB_PUPDR &=~0x0f;
	//*GPIOB_PUPDR |=0x05;
	//�����ٶ� ���٣�00��
	//*GPIOB_OSPEEDR &=~0X0F;
	//���������������0Ϊ����
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
