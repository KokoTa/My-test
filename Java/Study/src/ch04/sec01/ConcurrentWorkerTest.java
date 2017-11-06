package ch04.sec01;

public class ConcurrentWorkerTest {
    public static void main(String[] args) {
        // 实例化并调用方法
        ConcurrentWorker worker = new ConcurrentWorker();
        worker.work();
        System.out.println("Done");
    }
}
