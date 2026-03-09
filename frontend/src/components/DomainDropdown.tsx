import type { DomainOption } from "../types";

type DomainDropdownProps = {
  options?: DomainOption[];
  value?: string;
  onChange?: (value: string) => void;
};

export function DomainDropdown(_props: DomainDropdownProps) {
  return (
    <section className="domain-dropdown" aria-label="Domain selector">
      <strong>Domain Dropdown</strong>
    </section>
  );
}
