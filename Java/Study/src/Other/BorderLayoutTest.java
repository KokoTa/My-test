package Other;

import java.awt.*;

public class BorderLayoutTest extends Frame{
    public void init() {
        setLayout(new BorderLayout());
        add(new Button("top"), BorderLayout.NORTH);
        add(new Button("left"), BorderLayout.EAST);
        add(new Button("right"), BorderLayout.WEST);
        add(new Label("Center"), BorderLayout.SOUTH);
        String msg = "Greeting sir!";
        add(new TextArea(msg), BorderLayout.CENTER);
    }
    public BorderLayoutTest() {
        super("示例");
        init();
    }
    public static void main(String[] args) {
        BorderLayoutTest demo = new BorderLayoutTest();
        demo.setSize(400, 400);
        demo.setVisible(true);
    };
}
