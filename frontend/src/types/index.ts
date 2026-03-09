export type DomainOption = {
  label: string;
  value: string;
};

export type ContentType = "text" | "video" | "audio" | "applet";

export interface ContentCardData {
  id: string;
  title: string;
  type: ContentType;
  description?: string;
}
