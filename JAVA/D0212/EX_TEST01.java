/* *****************************************************************************************
 *  키보드 입력 받아서 조건에 해당 여부 결과 출력
 *  - Scanner 인스턴스 생성 : 표준입력 즉, System.in 스트림
 * **************************************************************************************** */

//모듈로딩
import java.util.Scanner;

public class EX_TEST01 {
	public static void main(String[] args) {
		
		// 스캐너 객체 생성
		Scanner in = new Scanner(System.in);
			
		// [1] 입력 받은 문자가 알파벳 대문자 여부 >> 'A' and 'Z'
		System.out.print("데이터 입력(예:A 9 7) : ");
		String data = in.next();
		char cdata = data.charAt(0);
		
		System.out.printf("%c 는 알파벳 대문자? %b %n",cdata, (cdata>='A') && (cdata <= 'Z'));
		
		
		// [2] 입력 받은 문자가 짝수인지 여부	>> %2 == 0
		int num = in.nextInt();
		System.out.printf("%d 는 짝수?, %b %n",num, num%2 == 0);
		
		
		// [3] 입력 받은 문자가 숫자(0 ~ 9) 여부	>> 0 and 9
		int num2 = in.nextInt();
		System.out.printf("%d 는 숫자?, %b %n",num2, (num2>=0) && (num2<=9));
		/*
		 * >출력결과>>
		 * 데이터 입력(예:A 9 7) : D 5 9
			D 는 알파벳 대문자? true 
			5 는 짝수?, false 
			9 는 숫자?, true 
		 */
		
		
		
//		//char타입으로도 가능, 같은 결과 출력
//		cdata = in.next().charAt(0);
//		System.out.printf("%c는 숫자? %b %n", cdata,(cdata>='0') && (cdata<='9'));

		 
		
		//Scanner 연결 해제
		in.close();
		
		
	}
}
