import javax.swing.*;
import java.awt.*;

public class ImagePanel extends JPanel {
    private Image img;
    private Image scaled;

//    public ImagePanel(String img){
//        this(new ImageIcon(img).getImage());
//    }

    public ImagePanel(Image img){
        this.img = img;
        setBackground(Color.lightGray);
    }

    @Override
    public void invalidate(){
        super.invalidate();
        int width = getWidth();
        int height = getHeight();

        if(width > 0 && height > 0){
            scaled = img.getScaledInstance(getWidth(), getHeight(),
                    Image.SCALE_FAST);

        }

    }

    @Override
    public Dimension getPreferredSize(){

        return img == null ? new Dimension(200,200) :
                new Dimension(img.getWidth(this), img.getHeight(this));

    }

    @Override
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        g.drawImage(scaled, 0, 0, null);
    }

}
