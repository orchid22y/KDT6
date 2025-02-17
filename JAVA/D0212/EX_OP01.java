/*
 * 연산자 - 비교연산자 & 논리연산자
 */
public class EX_OP01 {

	public static void main(String[] args) {
		// 비교 연산자
		int num1=30;
		int num2=7;
		
		// 비교 연산 결과 화면 출력
		
		System.out.printf("%d > %d :%b %n", num1, num2, num1>num2 );	// 30 > 7 :true 
		System.out.printf("%d < %d :%b %n", num1, num2, num1<num2 );	// 30 < 7 :false
		System.out.printf("%d >= %d :%b %n", num1, num2, num1>=num2 );	// 30 >= 7 :true 
		System.out.printf("%d <= %d :%b %n", num1, num2, num1<=num2 );	// 30 <= 7 :false
		System.out.printf("%d == %d :%b %n", num1, num2, num1==num2 );	// 30 == 7 :false 
		System.out.printf("%d != %d :%b %n", num1, num2, num1!=num2 );	// 30 != 7 :true
		
		// 논리 연산 결과 화면 출력
		// - num1이 짝수이면서 30이하 숫자 인지 여부
		// - num1 % 2 == 0 짝수, num1 % 2 == 1 홀수
		// - num1 <= 30
		// 논리연산자 앞뒤로는 Boolean 타입 데이터가 와야함
		
		System.out.println( num1%2 );		//	0
		System.out.println( num2 <= 30 );	// true
		System.out.printf("and 논리 연산자 && : %b %n", (num1%2==0) && (num1 <= 30));		// and 논리 연산자 && : true 
		System.out.printf("and 논리 연산자 && : %b %n\n", (num1%2==1) && (num1 <= 30));		// and 논리 연산자 && : false 
		
		// - '또는' 논리 연산자 ||
		System.out.printf("or 논리 연산자 || : %b %n", (num1%2 == 1) || (num1 <= 30));		// or 논리 연산자 || : true
		System.out.printf("or 논리 연산자 || : %b %n", (num1%2 == 0) || (num1 <= 30));		// or 논리 연산자 || : true 
		System.out.printf("or 논리 연산자 || : %b %n\n", (num1%2 == 1) || (num1 >= 30));		// or 논리 연산자 || : true
		
		// - XOR 논리 연산자 : ^ 둘 다 같은 결과 즉, 둘 다 True 이거나 둘 다 false이면 거짓
		//												true      ^		true
		System.out.printf("xor 논리 연산자 ^ : %b %n", (num1%2 == 0) ^ (num1 <= 30));		// xor 논리 연산자 ^ : false 
		//												false     ^		flase
		System.out.printf("xor 논리 연산자 ^ : %b %n", (num1%2 == 0) ^ (num1 <= 30));		// xor 논리 연산자 ^ : false 
		//												true      ^		flase
		System.out.printf("xor 논리 연산자 ^ : %b %n\n", (num1%2 == 0) ^ (num1 <= 30));		// xor 논리 연산자 ^ : false 
		
		
		
		// - Not 논리 연산자 : ! 현재 결과의 반대 Toggle
		System.out.printf("Not 논리연산자 ! : %b %n", !(num1%2==0));	// Not 논리연산자 ! : false 
		System.out.printf("Not 논리연산자 ! : %b %n\n", !(num1%2==1));	// Not 논리연산자 ! : true 
		
		
		// num1이 30대 인지 체크 => 30 ~ 39
		//System.out.printf("num1은 30대? %d %n",30<=num140);				//  문법 ERROR
		System.out.printf("num1은 30대? %b %n",(30<=num1)&&(num1<40));	// num1은 30대? true 
		
		
		
	}

}
