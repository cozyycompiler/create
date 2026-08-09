public class CozyJournal {

    static class Entry {
        String day;
        String mood;
        String thought;

        Entry(String day, String mood, String thought) {
            this.day = day;
            this.mood = mood;
            this.thought = thought;
        }

        void display() {
            System.out.println("╭────────────────────────────╮");
            System.out.println("  🌷 " + day);
            System.out.println("  Mood: " + mood);
            System.out.println("  \"" + thought + "\"");
            System.out.println("╰────────────────────────────╯");
        }
    }

    public static void main(String[] args) {

        Entry[] journal = {
            new Entry(
                "Monday",
                "☀️ Happy",
                "Today is a fresh beginning."
            ),

            new Entry(
                "Wednesday",
                "🌸 Calm",
                "Small progress is still progress."
            ),

            new Entry(
                "Friday",
                "🌙 Tired",
                "Rest is part of the journey."
            )
        };

        System.out.println("╔══════════════════════════════╗");
        System.out.println("║       🌷 MY COZY JOURNAL     ║");
        System.out.println("╚══════════════════════════════╝");

        for (Entry entry : journal) {
            entry.display();
        }

        System.out.println("\n✨ Remember:");
        System.out.println("   Be kind to yourself. ♡");
        System.out.println("   Keep growing at your own pace. 🌱");
    }
              }
