import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.awt.image.PixelGrabber;
import java.io.*;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.ArrayList;


public class IEEEProjectGUI extends JFrame {



    private JPanel InfoPanel = new JPanel();

    private ArrayList<JPanel> picsList = new ArrayList<>();

    private int picIndex = 0;


    private String githubLinkText = "For more information visit our Github " +
            "repository";

    private boolean InfoPanelShowing = true;

    private BufferedImage SOEPic;

    private BufferedImage AntennasPic;

    private BufferedImage ChamberPic;

    private BufferedImage LazerPic;

    private BufferedImage pondPic;

    private BufferedImage turntablePic;

    private BufferedImage backgroundPic;

    public void runCMD(ProcessBuilder pro){
        try {


            var process = pro.start();

            var reader =
                    new BufferedReader(new InputStreamReader(process.getInputStream()));

            String line;

            while ((line = reader.readLine()) != null) {
                System.out.println(line);

            }


        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }


    public void run(){

        setTitle("UNM APS 2019 Student Competition");
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();

        int screenWidth = (int)screenSize.getWidth();
        int screenHeight = (int)screenSize.getHeight();
        setSize((int)(screenWidth * 0.75), (int)(screenHeight * 0.75));

        S11Panel s11panel = new S11Panel();

        RadPatternPanel rpPanel = new RadPatternPanel();

        FinalResults finalResultsPanel = new FinalResults();



        JPanel MeasurementButtonHolders = new JPanel();

        JButton GoHome = new JButton("Back");

        JButton addFinalResults = new JButton("Results");

        JButton addRP = new JButton("Radiation Pattern Measurement");

        JButton addS11 = new JButton("S11 Measurement");

        JPanel ButtonHolder = new JPanel();

        MeasurementButtonHolders.setLayout(new GridLayout(0,2));

//        MeasurementButtonHolders.add(GoHome);
        MeasurementButtonHolders.add(addFinalResults);

        ButtonHolder.setLayout(new GridLayout(0,2));
        ButtonHolder.add(addRP);
        ButtonHolder.add(addS11);

        GoHome.addActionListener(e ->{
            if(rpPanel.RadPatternpanelShowing){
                remove(rpPanel);
                remove(MeasurementButtonHolders);
                add(InfoPanel, BorderLayout.CENTER);
                setTitle("UNM APS 2019 Student Competition");
                rpPanel.RadPatternpanelShowing = false;
                finalResultsPanel.FinalResultsPanelShowing = false;
                InfoPanelShowing = true;
                s11panel.S11PanelShowing = false;
                validate();

            }
            if(s11panel.S11PanelShowing){
                remove(s11panel);
                remove(MeasurementButtonHolders);
                add(InfoPanel, BorderLayout.CENTER);
                setTitle("UNM APS 2019 Student Competition");
                s11panel.S11PanelShowing = false;
                finalResultsPanel.FinalResultsPanelShowing = false;
                InfoPanelShowing = true;
                rpPanel.RadPatternpanelShowing = false;
                validate();

            }if(finalResultsPanel.FinalResultsPanelShowing){
                remove(finalResultsPanel);
                remove(GoHome);
                add(InfoPanel, BorderLayout.CENTER);
                setTitle("UNM APS 2019 Student Competition");
                s11panel.S11PanelShowing = false;
                finalResultsPanel.FinalResultsPanelShowing = false;
                InfoPanelShowing = true;
                rpPanel.RadPatternpanelShowing = false;
                validate();
            }

            System.setOut(System.out);
            System.setErr(System.err);
            validate();
            repaint();
        });


//        JPanel MeasurementButtonHolders = new JPanel();

//        JButton addFinalResults = new JButton("Results");
        addFinalResults.addActionListener(e ->{

            if(s11panel.S11PanelShowing){
                remove(s11panel);
                remove(MeasurementButtonHolders);
//                s11panel.S11PanelShowing = false;
            }else if(rpPanel.RadPatternpanelShowing){
                remove(rpPanel);
                remove(MeasurementButtonHolders);
//                rpPanel.RadPatternpanelShowing = false;
            }

            if(finalResultsPanel.checkifFileExists("s11Plot.png")){

                try {
                    finalResultsPanel.S11Pic =
                            ImageIO.read(new File(getClass().getResource(
                            "s11Plot.png").getFile()));
                }catch(IOException ee){

                }

                if(finalResultsPanel.S11PicCount < 1){


                    JPanel S11PicPanel = new ImagePanel(finalResultsPanel.S11Pic);

                    finalResultsPanel.add(S11PicPanel);


                    finalResultsPanel.S11PicCount++;
                }

            }

            if(finalResultsPanel.checkifFileExists("RadiationPattern2D.png")){

                try {
                    finalResultsPanel.RP2DPic =
                            ImageIO.read(new File(getClass().getResource(
                                    "RadiationPattern2D.png").getFile()));
                }catch(IOException ee){

                }

                if(finalResultsPanel.RP2DPicCount < 1){


                    JPanel RP2DPicPanel = new ImagePanel(finalResultsPanel.RP2DPic);

                    finalResultsPanel.add(RP2DPicPanel);


                    finalResultsPanel.RP2DPicCount++;
                }


            }

            if(finalResultsPanel.checkifFileExists("3DPatternImage.png")){

                try {
                    finalResultsPanel.RP3DPic =
                            ImageIO.read(new File(getClass().getResource(
                                    "3DPatternImage.png").getFile()));
                }catch(IOException ee){

                }

                if(finalResultsPanel.RP33DPicCount < 1){


                    JPanel RP3DPicPanel =
                            new ImagePanel(finalResultsPanel.RP3DPic);

                    RP3DPicPanel.addMouseListener(new MouseAdapter() {
                        @Override
                        public void mouseClicked(MouseEvent e) {
                            ClassLoader classLoader = getClass().getClassLoader();
                            File fi =
                                    new File(classLoader.getResource("open3DPlot").getFile());

                            runCMD(new ProcessBuilder(fi.toString()));
                        }
                    });

                    finalResultsPanel.add(RP3DPicPanel);


                    finalResultsPanel.RP33DPicCount++;
                }


            }



            setTitle("Results");
            add(finalResultsPanel, BorderLayout.CENTER);
            add(GoHome, BorderLayout.SOUTH);
            rpPanel.rptextfield.setText("Enter frequency in GHz");
            s11panel.s11textField.setText("Enter frequency in GHz");
            finalResultsPanel.FinalResultsPanelShowing = true;
            rpPanel.RadPatternpanelShowing = false;
            s11panel.S11PanelShowing = false;
            InfoPanelShowing = false;

            validate();
            repaint();


        });

        addRP.addActionListener(e -> {


            remove(InfoPanel);
            add(rpPanel, BorderLayout.CENTER);
            MeasurementButtonHolders.add(GoHome);
            add(MeasurementButtonHolders, BorderLayout.SOUTH);
            setTitle("Radiation Pattern Measurement");

            s11panel.S11PanelShowing = false;
            finalResultsPanel.FinalResultsPanelShowing = false;
            rpPanel.RadPatternpanelShowing = true;
            InfoPanelShowing = false;
            s11panel.s11textField.setText("Enter frequency in GHz");
            System.setOut(rpPanel.rpprintstream);
            System.setErr(rpPanel.rpprintstream);

            validate();

            repaint();

        });

//        JButton addS11 = new JButton("S11 Measurement");
        addS11.addActionListener(e -> {

            remove(InfoPanel);
            add(s11panel, BorderLayout.CENTER);
            MeasurementButtonHolders.add(GoHome);
            add(MeasurementButtonHolders, BorderLayout.SOUTH);
            setTitle("S11 Measurement");
            InfoPanelShowing = false;
            rpPanel.RadPatternpanelShowing = false;
            finalResultsPanel.FinalResultsPanelShowing = false;
            s11panel.S11PanelShowing = true;
            rpPanel.rptextfield.setText("Enter frequency in GHz");
            System.setOut(s11panel.S11PrintStream);
            System.setErr(s11panel.S11PrintStream);
            validate();
            repaint();
        });





        JLabel openGithubLink = new JLabel(githubLinkText);
        openGithubLink.setHorizontalAlignment(SwingConstants.CENTER);
        openGithubLink.setVerticalAlignment(SwingConstants.CENTER);
        openGithubLink.setForeground(Color.BLUE.darker());
        openGithubLink.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));

        openGithubLink.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try{
                    Desktop.getDesktop().browse(new URI("https://github.com/jargyres/UNM-IEEE-APS-Student-Competiton-2019"));
                }catch(IOException | URISyntaxException e1){
                    JOptionPane.showMessageDialog(InfoPanel, e1.getStackTrace());
                }
            }
            @Override
            public void mouseExited(MouseEvent e){
                openGithubLink.setText(githubLinkText);
            }

            @Override
            public void mouseEntered(MouseEvent e){
                openGithubLink.setText("<html><a href = ''>" + githubLinkText + "</a></html>");
            }
        });

        try {
            SOEPic = ImageIO.read(new File(getClass().getResource("new-soe" +
                    "-logo.png").getFile()));
        }catch(IOException e){

        }

        try{
            AntennasPic = ImageIO.read(new File(getClass().getResource(
                    "Antennaslogo.png").getFile()));
        }catch(IOException e){

        }
        try{
            ChamberPic = ImageIO.read(new File(getClass().getResource(
                    "Chamber.jpeg").getFile()));
        }catch(IOException e){

        }
        try{
            LazerPic = ImageIO.read(new File(getClass().getResource(
                    "Lazer.jpeg").getFile()));
        }catch(IOException e){

        }
        try{
            turntablePic = ImageIO.read(new File(getClass().getResource(
                    "table.jpg").getFile()));
        }catch(IOException e){

        }
        try{
            pondPic = ImageIO.read(new File(getClass().getResource(
                    "pond.jpg").getFile()));
        }catch(IOException e){

        }

        try{
            backgroundPic = ImageIO.read(new File(getClass().getResource(
                    "background.png").getFile()));
        }catch(IOException e){

        }



//        JPanel SOEPicPanel = new ImagePanel(SOEPic);
//
////        SOEPicPanel.setBackground();
//
//        picsList.add(SOEPicPanel);
//
//        JPanel AntennasPicPanel = new ImagePanel(AntennasPic);
//
//        picsList.add(AntennasPicPanel);
        JPanel backgroundPicPanel = new ImagePanel(backgroundPic);

        picsList.add(backgroundPicPanel);

        JPanel ChamberPicPanel = new ImagePanel(ChamberPic);

        picsList.add(ChamberPicPanel);

        JPanel LazerPicPanel = new ImagePanel(LazerPic);

        picsList.add(LazerPicPanel);

        JPanel turntablePanel = new ImagePanel(turntablePic);

        picsList.add(turntablePanel);

        JPanel pondPicPanel = new ImagePanel(pondPic);

        picsList.add(pondPicPanel);



        JPanel BlankPanel = new JPanel();

        BlankPanel.setBackground(Color.lightGray);

        JPanel PicHolder = new JPanel(new GridLayout(1,2));
//        JPanel PicHolder = new JPanel();

        PicHolder.setBackground(Color.lightGray);

        PicHolder.add(backgroundPicPanel, BorderLayout.CENTER);
//        PicHolder.add(BlankPanel);
//        PicHolder.add(AntennasPicPanel);

        InfoPanel.setLayout(new BorderLayout());

        InfoPanel.setBackground(Color.lightGray);




        InfoPanel.add(ButtonHolder, BorderLayout.SOUTH);

        InfoPanel.add(PicHolder, BorderLayout.CENTER);

        InfoPanel.add(openGithubLink, BorderLayout.NORTH);



        // end the setup for the info panel
//        JButton switchPicture = new JButton("Switch Picture");
//        PicHolder.add(switchPicture, BorderLayout.EAST);

        PicHolder.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                PicHolder.remove(picsList.get(picIndex));
//                PicHolder.remove(switchPicture);
                if(picIndex >= picsList.size()-1){
                    picIndex = -1;
                }
                picIndex ++;
                PicHolder.add(picsList.get(picIndex));
//                PicHolder.add(switchPicture, BorderLayout.LINE_END);

                validate();
                repaint();
            }
        });

        setLocation(10, 200);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        add(InfoPanel, BorderLayout.CENTER);

        setVisible(true);

    }

    public static void main(String[] args){

        IEEEProjectGUI jPanelTest = new IEEEProjectGUI();

        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {

                jPanelTest.run();

            }
        });

    }
}
