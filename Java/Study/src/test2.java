import java.io.File;
import java.io.IOException;

public class test2 {
    public static void method() {
        File x = new File("./file.txt");
        try {
            x.createNewFile();
        } catch (IOException e) {
            System.out.println("Error");
        }

    }

    public static void main(String[] args) {
        method();
    }
}
