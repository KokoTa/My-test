package Other;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class EventTest {
    static class handle implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            System.out.println("OK");
        }
    }
    public static void main(String[] args) {
        Frame f = new Frame("Test");
        Button b = new Button("Click me");
        b.addActionListener(new handle());
        f.setLayout(new FlowLayout());
        f.add(b);
        f.setSize(200, 200);
        f.setVisible(true);
    }
}
