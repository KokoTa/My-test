package Other;

import java.io.*;

public class InputOutput {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new FileWriter("input.txt"));


        String s;
        while(true) {
            System.out.println("请输入：");
            System.out.flush();
            s = br.readLine();
            if(s.length() == 0) break;
            bw.write(s);
            bw.newLine();
        }
        bw.close();

    }
}
