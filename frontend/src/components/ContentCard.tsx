import type { ContentCardData } from "../types";

type ContentCardProps = {
  item?: ContentCardData;
};

export function ContentCard(_props: ContentCardProps) {
  return (
    <article className="content-card" aria-label="Content card">
      <strong>Content Card</strong>
    </article>
  );
}
