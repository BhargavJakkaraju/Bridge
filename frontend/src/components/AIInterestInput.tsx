type AIInterestInputProps = {
  value?: string;
  onChange?: (value: string) => void;
};

export function AIInterestInput(_props: AIInterestInputProps) {
  return (
    <section className="ai-interest-input" aria-label="AI expertise input">
      <strong>AI Expertise Input</strong>
    </section>
  );
}
