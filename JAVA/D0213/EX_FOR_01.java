/*	***************************************************************************************
 * 	반복문 - for 반복문
 * 	***************************************************************************************/
public class EX_FOR_01 {

	public static void main(String[] args) {
		// 1 ~ 10까지 화면 출력
//		System.out.println(1);
//		System.out.println(2);
//		System.out.println(3);
//		System.out.println(4);
//		System.out.println(5);
//		System.out.println(6);
//		System.out.println(7);
//		System.out.println(8);
//		System.out.println(9);
//		System.out.println(10);
		
		
		for(int n=1; n<=10; n++)
			System.out.println(n);
		
		//1 ~50 범위에서 3의 배수만 출력 (3,6,9,12,...)
		//ver1
		for(int n=3;n<=50;n+=3)
			System.out.println(n);
		
		//ver2
		for(int n=1; n<=50; n++)
		{if(n%3 == 0)
				System.out.println(n);
		}
	}

}
