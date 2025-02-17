/*	***********************************************************************************
 * 	제어문 - 라벨 문
 * 			다중 중첩 반복문의 경우 한번에 모든 반복문을 빠져나가는 문법
 * 			break 라벨명;
 *	***********************************************************************************/
public class EX_Break {

	public static void main(String[] args) {
		// 중첩 반복문과 break문
		
		// 1개의 반복문만 중단하는 경우
		LABEL:
		for(int dan=2; dan<10; dan++)
			{
				for(int n=1; n<10; n++)
				{
					if(dan*n%7==0) {
						System.out.println("---END---");
						break LABEL; // for문 밖 LABEL로 이동
					}
						
					System.out.printf("%d * %d = %d %n", dan, n, dan*n);
				}
			}
			
			System.out.println("OK");

		
			
			
			
			
			
	}

}
