import java.util.*;

public class test{
	public static void main(String args[]){

		Scanner sc=new Scanner(System.in);

		System.out.println("enter int ");
		int tmp=sc.nextInt();

		sc.nextLine(); // need this otherwise String skipped after int inputted

		String lund=sc.nextLine();

		System.out.println("INPUTTED Int "+tmp+" String is "+lund);
	}
}