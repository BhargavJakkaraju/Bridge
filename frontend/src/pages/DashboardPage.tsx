import { AIInterestInput } from "../components/AIInterestInput";
import { ContentCard } from "../components/ContentCard";
import { DomainDropdown } from "../components/DomainDropdown";
import { FeedContainer } from "../components/FeedContainer";
import { Navbar } from "../components/Navbar";

export function DashboardPage() {
  return (
    <main className="page-shell" aria-label="Dashboard page shell">
      <Navbar />
      <DomainDropdown />
      <AIInterestInput />
      <FeedContainer>
        <ContentCard />
      </FeedContainer>
    </main>
  );
}
