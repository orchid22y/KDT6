/*	*******************************************************************************************
 * 	제어문 - 	for 반복문
 *	*******************************************************************************************/
public class EX_FOR_03 {

	public static void main(String[] args) {
		// 구구단 출력 하기 
		
		for(int n=0;n<20;n++)
		{	
			int mock=n/10;
			for(int dan=2+4*mock;dan<=5+4*mock;dan++)
			{
				if (n%10==0)
					System.out.printf("   [%d단]   %c", dan,((dan==5)||(dan==9))?'\n':'\t');
				else
					System.out.printf("%d + %d = %d %c", dan, n%10, dan*n%10,((dan==5)||(dan==9))?'\n':'\t');
			}
			
		}
		


	}

}

