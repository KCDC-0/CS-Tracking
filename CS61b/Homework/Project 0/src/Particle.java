package src;
//import edu.princeton.cs.algs4.StdRandom;

import java.awt.*;
import java.util.Map;

public class Particle {
    public ParticleFlavor flavor;
    public int lifespan;

    public static final int PLANT_LIFESPAN = 150;
    public static final int FLOWER_LIFESPAN = 75;
    public static final int FIRE_LIFESPAN = 10;
    public static final Map<ParticleFlavor, Integer> LIFESPANS =
            Map.of(ParticleFlavor.FLOWER, FLOWER_LIFESPAN,
                   ParticleFlavor.PLANT, PLANT_LIFESPAN,
                   ParticleFlavor.FIRE, FIRE_LIFESPAN);

    public Particle(ParticleFlavor flavor) {
        this.flavor = flavor;
        lifespan = -1;
    }

    public Color color() {
        switch (this.flavor) {
            case EMPTY:
                return Color.BLACK;
            case SAND:
                return Color.YELLOW;
            case BARRIER:
                return Color.GRAY;
            case WATER:
                return Color.BLUE;
            case FOUNTAIN:
                return Color.CYAN;
            case PLANT:
                return new Color(0, 255, 0);
            case FIRE:
                return new Color(255, 0, 0);
            case FLOWER:
                return new Color(255, 141, 161);
            default:
                return Color.BLACK;
        }
    }

    public void moveInto(Particle other) {
        if (other == null) {
            return;
        }

        other.flavor = this.flavor;
        other.lifespan = this.lifespan;

        this.flavor = ParticleFlavor.EMPTY;
        this.lifespan = -1;
    }

    public void fall(Map<Direction, Particle> neighbors) {
        Particle downNeighbor = neighbors.get(Direction.DOWN);
        if (downNeighbor != null && downNeighbor.flavor == ParticleFlavor.EMPTY) {
            this.moveInto(downNeighbor);
        }
    }

    public void flow(Map<Direction, Particle> neighbors) {
        Particle leftNeighbor = neighbors.get(Direction.LEFT);
        Particle rightNeighbor = neighbors.get(Direction.RIGHT);
        
        boolean canMoveLeft = (leftNeighbor != null && leftNeighbor.flavor == ParticleFlavor.EMPTY);
        boolean canMoveRight = (rightNeighbor != null && rightNeighbor.flavor == ParticleFlavor.EMPTY);

        if (canMoveLeft && canMoveRight) {
            if (Math.random() < 0.5) {
                this.moveInto(leftNeighbor);
            } else {
                this.moveInto(rightNeighbor);
            }
        } else if (canMoveLeft) {
            this.moveInto(leftNeighbor);
        } else if (canMoveRight) {
            this.moveInto(rightNeighbor);
        }
    }

    public void grow(Map<Direction, Particle> neighbors) {
    }

    public void burn(Map<Direction, Particle> neighbors) {
    }

    public void action(Map<Direction, Particle> neighbors) {
        if (this.flavor == ParticleFlavor.EMPTY) {
            return;
        }

        if (this.flavor != ParticleFlavor.BARRIER) {
            this.fall(neighbors);
        }

        if (this.flavor == ParticleFlavor.WATER) {
            this.flow(neighbors);
        }
    }
}