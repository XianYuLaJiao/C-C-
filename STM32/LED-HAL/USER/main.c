#include "sys.h"
#include "delay.h"
#include "usart.h"

/************************************************
 ALIENTEK ������STM32F429������ʵ��0-1
 Template����ģ��-�½������½�ʹ��-HAL��汾
 ����֧�֣�www.openedv.com
 �Ա����̣� http://eboard.taobao.com 
 ��ע΢�Ź���ƽ̨΢�źţ�"����ԭ��"����ѻ�ȡSTM32���ϡ�
 ������������ӿƼ����޹�˾  
 ���ߣ�����ԭ�� @ALIENTEK
************************************************/


/***ע�⣺�����̺ͽ̳��е��½�����3.3С�ڶ�Ӧ***/


void Delay(__IO uint32_t nCount);

void Delay(__IO uint32_t nCount)
{
  while(nCount--){}
}


int main(void)
{
	
  GPIO_InitTypeDef GPIOINITB;
	
	HAL_Init();                     //��ʼ��HAL��    
  Stm32_Clock_Init(360,25,2,8);   //����ʱ��,180Mhz
	
	__HAL_RCC_GPIOB_CLK_ENABLE();  //��gpiob��ʱ��
	delay_init(180);
	
	
	GPIOINITB.Pin  = GPIO_PIN_0|GPIO_PIN_1;
	GPIOINITB.Mode = GPIO_MODE_OUTPUT_PP;
	GPIOINITB.Pull = GPIO_PULLUP;
	GPIOINITB.Speed= GPIO_SPEED_HIGH;
	
	HAL_GPIO_Init(GPIOB,&GPIOINITB);

	do
	{
		HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_SET);
		HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_SET);
		Delay(0xffffff);
		HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_RESET);
		HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_RESET);
		Delay(0xffffff);
	}while(1);
		
}

