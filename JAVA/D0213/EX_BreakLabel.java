/*	***********************************************************************************
 * 	제어문 - break문
 * 			가장 가까이에 있는 반복문 종료함
 * 			중첩의 경우 가까이 있는 반복문만 종료
 *	***********************************************************************************/
public class EX_BreakLabel {

	public static void main(String[] args) {
		// 중첩 반복문과 break문
		// 1개의 반복문만 중단하는 경우
			for(int dan=2; dan<10; dan++)
			{
				for(int n=1; n<10; n++)
				{
					if(dan*n%7==0) {
						System.out.println("---END---");
						break;
					}
						
					System.out.printf("%d * %d = %d %n", dan, n, dan*n);
				}
			}
			
		// 반복문 모두 중단하는 경우
		// 내부에 반복문 중단여부 정보 저장 변수	
			
		boolean isEnd = false;	
		for(int dan=2; dan<10; dan++)
		{
			//밖의 for문은 안의 for문이 종료되었으면 종료하기 ==>Flag 변수
			
			if (isEnd==true)break;
			for(int n=1; n<10; n++)
			{
				if(dan*n%7==0) {
					System.out.println("---END---");
					isEnd=true;
					break;
				}
					
				System.out.printf("%d * %d = %d %n", dan, n, dan*n);
			}
		}
			
			
			
			
			
	}

}
