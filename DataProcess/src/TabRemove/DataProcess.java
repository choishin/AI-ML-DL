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
		
		String path = "C:\\Users\\chois\\OneDrive\\���� ȭ��\\test.csv";
		String path2 = "C:\\Users\\chois\\OneDrive\\���� ȭ��\\test_remove.csv";
		String line;
		BufferedReader reader = new BufferedReader(new FileReader(path));
		BufferedWriter writer = new BufferedWriter(new FileWriter(path2,true));
		ArrayList<String> lines = new ArrayList<String>();

		//1. �ڷ� ���پ� �ް� ArrayList�� �ֱ�
		while ((line = reader.readLine()) != null) {
			String[] column = line.split(",");
			lines.add(line.replace("\t", "").replace("\"", ""));
		}

		//2. ���پ� �Ǿ��ִ� �ڷḦ ,�� �߶� String[][] �� �ֱ�
		String[][] words = new String[lines.size()][];

		for (int i = 0; i<lines.size(); i++) {	
			//�ڷḦ �޸��������� �߶� �ְ�
			words[i] = lines.get(i).split(",");
			//�߶� ���� �ڷ��� ���� 3�� �̻��� ���� �ǳʶڴ�.
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
