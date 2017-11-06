package ch04.sec01;

public class ConcurrentWorker extends Worker {
    public void work() {
        // 利用Thread构造一个线程
        Thread t = new Thread(super::work); // 传入父类的work方法
        t.start(); // 启动线程
    }
}