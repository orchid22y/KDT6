
import java.util.Scanner;

public class EX_While_01 {

	public static void main(String[] args) {
		// 키보드로 숫자 입력 받은 후 평균, 합계 출력
		// 단, 0 입력 시 입력 받기 종료
		
		Scanner keyboard = new Scanner(System.in);

		// 반복 횟수, 입력 값 저장 변수
		int count=0;		// 입력 갯수 저장
		int total=0;		// 입력 값 누적 저장
		float avg=0.f;		// 평균 저장
		
		int data = 0;		// 현재 입력값 저장
		
		while((data=keyboard.nextInt()) !=0)
		{
			total += data;
			count++;
		}
		
		
	
		// 입력 종료 후 합계, 평균 계산 후 출력
		avg = (float)total/count;
		System.out.printf("합계 : %d, 평균 : %f %n", total,avg);
		
		//ver2
		
		// 반복 횟수, 입력 값 저장 변수
		count=0;		// 입력 갯수 저장
		total=0;		// 입력 값 누적 저장
		avg=0.f;		// 평균 저장
		
		data = 0;		// 현재 입력값 저장
		
		while(true)
		{
			System.out.print("숫자 입력:");
			if((data=keyboard.nextInt())==0)
				break;
			total += data;
			count++;
		}
		
		// 입력 종료 후 합계, 평균 계산 후 출력
			avg = (float)total/count;
			System.out.printf("합계 : %d, 평균 : %f %n", total,avg);
	
			
		keyboard.close();
				
		
		
	}
	
}
