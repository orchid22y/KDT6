/* ******************************************************************************
 * 연산자 - 증감연산자
 * - ++ 1증가
 * - -- 1감소
 * ***************************************************************************** */
public class EX_08 {

	public static void main(String[] args) {
		// 변수 선언 및 초기화
		int num = 100;
		
		// 화면에 출력
		System.out.printf("(0) num is %d\n", num);			// (0) num is 100	// 초기화 된 num 출력
		System.out.printf("(1) num is %d\n", ++num);		// (1) num is 101	// ++으로 먼저 1증가 후 %d에 전달 :선증가
		System.out.printf("(2) num is %d\n\n", num);		// (2) num is 101	
		
		System.out.printf("(3) num is %d\n", num++);		// (3) num is 101	// %d에 전달 후 1증가 : 후증가
		System.out.printf("(4) num is %d\n\n", num);		// (4) num is 102
		
		System.out.printf("(5) num is %d\n", num--);		// (5) num is 102	// %d에 전달 후 1감소 : 후감소
		System.out.printf("(6) num is %d\n\n", num);		// (6) num is 101
		
		System.out.printf("(7) num is %d\n", --num);		// (5) num is 100	// 1감소 후 %d에 전달 : 선감소
		System.out.printf("(8) num is %d\n\n", num);		// (6) num is 100
		
	}

}
