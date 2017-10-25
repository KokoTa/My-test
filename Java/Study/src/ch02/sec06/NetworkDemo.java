package ch02.sec06;

public class NetworkDemo {
    public static void main(String[] args) {
        Network myFace = new Network(); // 创建网络
        Network tooter = new Network(); // 创建网络
        Network.Member fred = myFace.enroll("Fred"); // 新建对象放入网络myFace的数组列表，并返回这个新建对象
        Network.Member wilma = myFace.new Member("Wilma"); // 新建对象
            // An object, but not enrolled
            // Make the constructor private to avoid this
        fred.addFriend(wilma); // 将wilma放入fred这个对象的数组列表中

        Network.Member barney = tooter.enroll("Barney"); // 新建对象放入网络tooter的数组列表，并返回这个新建对象
        fred.addFriend(barney); // 将barney放入fred这个对象的数组列表中
        System.out.println(myFace); // 默认调用toString()方法
            // If it shouldn't be possible to add a friend
            // from another network, call belongsTo
        System.out.println(barney.belongsTo(myFace)); // 两者不属于同一个网络，返回false
    }
}
