package Other;

import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.Date;

public class URLtest {
    public static void main(String[] args)  {
        String url = "http://www.baidu.com";
        URL hp = null;
        try {
            hp = new URL(url);
        } catch (MalformedURLException e) {
            System.out.println(e.getMessage());
        }
        URLConnection hpc = null;
        try {
            hpc = hp.openConnection();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        System.out.println(new Date(hpc.getDate()));
        System.out.println(hpc.getContentType());
        System.out.println(hpc.getExpiration());
        System.out.println(new Date(hpc.getLastModified()));
        int len = hpc.getContentLength();
        if(len > 0) {
            try {
                InputStream input = hpc.getInputStream();
                int i = len;
                int c = 0;
                while(((c=input.read()) != -1) && i > 0) {
                    System.out.println((char) c);
                    i--;
                }
            } catch (IOException e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("No content");
        }
    }
}
