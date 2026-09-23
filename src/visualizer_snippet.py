import matplotlib.pyplot as plt
import seaborn as sns  # For better styling
import pandas as pd


class AITutorEvaluator:
    # Keep the rest of the original class methods here.

    def visualize_accuracy(self, save_path="accuracy_report.png"):
        """Generate visual accuracy report with multiple plots."""
        df = pd.DataFrame(self.results)

        # Set up the figure
        plt.figure(figsize=(15, 10))
        plt.suptitle('AI Tutor Performance Evaluation', y=1.02, fontsize=14)

        # Plot 1: Accuracy by Question
        plt.subplot(2, 2, 1)
        ax = sns.barplot(
            data=df,
            x=df.index,
            y='Keyword Accuracy',
            hue='Difficulty',
            palette='viridis'
        )
        plt.title('Accuracy per Question')
        plt.ylabel('Accuracy Score')
        plt.xlabel('Question Index')
        plt.ylim(0, 1)

        # Add value labels
        for p in ax.patches:
            ax.annotate(
                f"{p.get_height():.0%}",
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points'
            )

        # Plot 2: Accuracy Distribution
        plt.subplot(2, 2, 2)
        sns.boxplot(
            data=df,
            y='Keyword Accuracy',
            palette='pastel'
        )
        plt.title('Overall Accuracy Distribution')
        plt.ylabel('Accuracy Score')

        # Plot 3: Missing Keywords Heatmap
        plt.subplot(2, 2, 3)
        all_keywords = list(set(kw for case in TEST_CASES for kw in case["expected_keywords"]))
        keyword_presence = []

        for _, row in df.iterrows():
            keyword_presence.append([
                kw.lower() in row['Response'].lower()
                for kw in all_keywords
            ])

        sns.heatmap(
            keyword_presence,
            annot=True,
            cmap='YlGnBu',
            xticklabels=all_keywords,
            yticklabels=[f"Q{i+1}" for i in range(len(df))]
        )
        plt.title('Keyword Coverage')
        plt.xlabel('Keywords')
        plt.ylabel('Questions')

        # Plot 4: Difficulty Analysis
        plt.subplot(2, 2, 4)
        sns.barplot(
            data=df.groupby('Difficulty')['Keyword Accuracy'].mean().reset_index(),
            x='Difficulty',
            y='Keyword Accuracy',
            palette='rocket'
        )
        plt.title('Accuracy by Difficulty Level')
        plt.ylabel('Average Accuracy')
        plt.ylim(0, 1)

        # Adjust layout and save
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n📈 Visualization saved to {save_path}")
        plt.show()


# Integration requirements:
# - Add the remaining original AITutorEvaluator methods.
# - Define TEST_CASES with expected_keywords.
# - Populate self.results with Keyword Accuracy, Difficulty, and Response.
# This excerpt alone is not a complete runnable tutor application.
