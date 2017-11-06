package ch04.sec04;

import java.io.UnsupportedEncodingException;
import java.util.ServiceLoader;

public class ServiceLoaderDemo {
    // 服务器类加载的内容保存在META-INF.services里
    // 加载Cipher.class，然后就能调用类的方法了
    public static ServiceLoader<Cipher> cipherLoader = ServiceLoader.load(Cipher.class);

    public static void main(String[] args) throws UnsupportedEncodingException {
        Cipher ciph = getCipher(1); // 加载类
        String message = "Meet me at the toga party."; // 待加密字符串
        byte[] bytes = ciph.encrypt(message.getBytes(), new byte[] { 3 }); // 加密
        String encrypted = new String(bytes, "UTF-8"); // 转换
        System.out.println(encrypted); // 打印加密后的字符串
    }
    
    public static Cipher getCipher(int minStrength) { // 控制加在次数
        for (Cipher cipher : cipherLoader) // .rm Implicitly calls iterator 隐式调用迭代器
            if (cipher.strength() >= minStrength) return cipher;
        return null;
    }
}
