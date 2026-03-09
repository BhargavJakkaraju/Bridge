import { useEffect, useMemo, useState } from "react";
import type { Session } from "@supabase/supabase-js";

import { isSupabaseConfigured, supabase } from "../lib/supabase";

export function useAuth() {
  const [session, setSession] = useState<Session | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!supabase) {
      setLoading(false);
      return;
    }

    let mounted = true;

    supabase.auth.getSession().then(({ data }) => {
      if (!mounted) {
        return;
      }
      setSession(data.session);
      setLoading(false);
    });

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, nextSession) => {
      setSession(nextSession);
      setLoading(false);
    });

    return () => {
      mounted = false;
      subscription.unsubscribe();
    };
  }, []);

  const value = useMemo(
    () => ({
      session,
      user: session?.user ?? null,
      loading,
      isConfigured: isSupabaseConfigured,
      signUp: async (email: string, password: string) => {
        if (!supabase) {
          return {
            data: { user: null, session: null },
            error: new Error("Supabase is not configured."),
          };
        }
        return supabase.auth.signUp({ email, password });
      },
      signIn: async (email: string, password: string) => {
        if (!supabase) {
          return {
            data: { user: null, session: null },
            error: new Error("Supabase is not configured."),
          };
        }
        return supabase.auth.signInWithPassword({ email, password });
      },
      signOut: async () => {
        if (!supabase) {
          return { error: null };
        }
        return supabase.auth.signOut();
      },
    }),
    [loading, session],
  );

  return value;
}
