import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;

public class TypingVideo {
    public static void main(String[] args) throws Exception {
        int width = 1080;
        int height = 1920;
        String text = "Transforme seu futuro em código!";
        int fps = 24;
        int charsPerSecond = 10;

        // Calcula duração total em segundos
        int totalFrames = (int) ((text.length() / (double) charsPerSecond) * fps) + fps;

        // Fonte
        Font font = new Font("Arial", Font.BOLD, 64);

        for (int frame = 0; frame < totalFrames; frame++) {
            BufferedImage img = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
            Graphics2D g = img.createGraphics();

            // Fundo gradiente
            GradientPaint gp = new GradientPaint(0, 0, new Color(18, 24, 45),
                                                 0, height, new Color(88, 35, 125));
            g.setPaint(gp);
            g.fillRect(0, 0, width, height);

            // Quantos caracteres mostrar neste frame
            int visibleChars = Math.min(text.length(), (int) ((frame / (double) fps) * charsPerSecond));
            String partialText = text.substring(0, visibleChars);

            // Texto centralizado
            g.setFont(font);
            g.setColor(Color.WHITE);
            FontMetrics fm = g.getFontMetrics();
            int x = (width - fm.stringWidth(partialText)) / 2;
            int y = height / 2;
            g.drawString(partialText, x, y);

            g.dispose();

            // Salva frame
            String filename = String.format("frames/frame_%05d.png", frame);
            new File("frames").mkdirs();
            ImageIO.write(img, "png", new File(filename));
        }

        System.out.println("Frames gerados em /frames. Agora use FFmpeg para juntar em vídeo:");
        System.out.println("ffmpeg -r " + fps + " -i frames/frame_%05d.png -c:v libx264 -pix_fmt yuv420p reel_typing.mp4");
    }
}
