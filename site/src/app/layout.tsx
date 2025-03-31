export const metadata = {
  title: "CANW – Complexity And Network Webdesign",
  description:
    "Exploring biological, cultural, and emergent complexity on the web.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
