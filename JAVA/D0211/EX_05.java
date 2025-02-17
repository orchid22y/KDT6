/* ***********************************************************************************
 *  키보드로 입력 받기
 *  - 추가 패키지 필요	: java.utill.Scanner 클래스
 *  - 객체 생성 필요 	: new Scanner(System.in)
 * ********************************************************************************** */

// 패키지 로딩
import java.util.Scanner;


// 메인 클래스
public class EX_05 {

	public static void main(String[] args) {
		
		//Scanner 객체 생성
		Scanner scan = new Scanner(System.in);	//Scanner객체를 생성 했기 때문에 타입명도 Scanner
		
		// 입력받고 싶은 요청 메세지 출력
		System.out.print("이름, 나이 입력: ");
		
		// 스캐너로 가져오기
		String name = scan.next();
		int nage = scan.nextInt();
		
		
		
		// 출력 하기
		System.out.println(name);
		System.out.println(nage);
		
		//입력 스트림 닫기
		scan.close();
	}

}
