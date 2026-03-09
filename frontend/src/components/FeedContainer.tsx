import type { ReactNode } from "react";

type FeedContainerProps = {
  children?: ReactNode;
};

export function FeedContainer({ children }: FeedContainerProps) {
  return (
    <section className="feed-container">
      <strong>Feed Container</strong>
      {children}
    </section>
  );
}
