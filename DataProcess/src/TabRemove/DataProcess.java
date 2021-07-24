package TabRemove;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class DataProcess {
	
	public static void main (String[] args) throws IOException {
		
		fileMake();
		
	}
	
	public static void fileMake() throws IOException {
		
		String path = "C:\\Users\\chois\\OneDrive\\바탕 화면\\test.csv";
		String path2 = "C:\\Users\\chois\\OneDrive\\바탕 화면\\test_remove.csv";
		String line;
		BufferedReader reader = new BufferedReader(new FileReader(path));
		BufferedWriter writer = new BufferedWriter(new FileWriter(path2,true));
		ArrayList<String> lines = new ArrayList<String>();

		//1. 자료 한줄씩 받고 ArrayList에 넣기
		while ((line = reader.readLine()) != null) {
			String[] column = line.split(",");
			lines.add(line.replace("\t", "").replace("\"", ""));
		}

		//2. 한줄씩 되어있는 자료를 ,로 잘라서 String[][] 에 넣기
		String[][] words = new String[lines.size()][];

		for (int i = 0; i<lines.size(); i++) {	
			//자료를 콤마기준으로 잘라서 넣고
			words[i] = lines.get(i).split(",");
			//잘라서 넣은 자료의 행이 3개 이상이 들어가면 건너뛴다.
			if (words[i].length != 3) {
				continue;
			}
			else {
			writer.append(Arrays.toString(words[i])+",");
			writer.newLine();
			}
			System.out.println(Arrays.toString(words[i]));	
		}
		
		writer.close();
	}
	
}
