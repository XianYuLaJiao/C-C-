#include "sys.h"
#include "delay.h"
#include "usart.h"

/************************************************
 ALIENTEK 阿波罗STM32F429开发板实验0-1
 Template工程模板-新建工程章节使用-HAL库版本
 技术支持：www.openedv.com
 淘宝店铺： http://eboard.taobao.com 
 关注微信公众平台微信号："正点原子"，免费获取STM32资料。
 广州市星翼电子科技有限公司  
 作者：正点原子 @ALIENTEK
************************************************/


/***注意：本工程和教程中的新建工程3.3小节对应***/


void Delay(__IO uint32_t nCount);

void Delay(__IO uint32_t nCount)
{
  while(nCount--){}
}


int main(void)
{
	
  GPIO_InitTypeDef GPIOINITB;
	
	HAL_Init();                     //初始化HAL库    
  Stm32_Clock_Init(360,25,2,8);   //设置时钟,180Mhz
	
	__HAL_RCC_GPIOB_CLK_ENABLE();  //打开gpiob的时钟
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

