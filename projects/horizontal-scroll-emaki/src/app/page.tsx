"use client";

import dynamic from "next/dynamic";

const KonvaEmakiViewer = dynamic(
  () => import("../components/KonvaEmakiiViewer"),
  {
    ssr: false,
  }
);

export default function page() {
  return (
    <main
      style={{ width: "100vw", height: "100vh", backgroundColor: "#f4f4f4" }}
    >
      <KonvaEmakiViewer />
    </main>
  );
}
